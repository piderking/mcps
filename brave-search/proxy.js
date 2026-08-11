import http from 'node:http';
import { spawn } from 'node:child_process';

const PUBLIC_PORT = parseInt(process.env.PORT || '8080');
const INTERNAL_PORT = 8081;

process.env.PORT = String(INTERNAL_PORT);

const command = process.argv.slice(2).join(' ');
console.log(`Starting Proxy on port ${PUBLIC_PORT} -> Supergateway on internal port ${INTERNAL_PORT}...`);

const sg = spawn('npx', [
  '-y', 'supergateway',
  '--port', String(INTERNAL_PORT),
  '--cors',
  '--outputTransport', 'streamableHttp',
  '--stdio', command
], {
  stdio: 'inherit',
  shell: true,
  env: process.env
});

sg.on('exit', (code) => {
  process.exit(code || 0);
});

const server = http.createServer((req, res) => {
  const existingAccept = req.headers['accept'] || '*/*';
  const hasJson = existingAccept.includes('application/json');
  const hasSse = existingAccept.includes('text/event-stream');

  let newAccept = existingAccept;
  if (!hasJson) newAccept += ', application/json';
  if (!hasSse) newAccept += ', text/event-stream';
  
  req.headers['accept'] = newAccept;

  const options = {
    hostname: '127.0.0.1',
    port: INTERNAL_PORT,
    path: req.url,
    method: req.method,
    headers: req.headers
  };

  const proxyReq = http.request(options, (proxyRes) => {
    res.writeHead(proxyRes.statusCode, proxyRes.headers);
    proxyRes.pipe(res, { end: true });
  });

  proxyReq.on('error', (err) => {
    if (!res.headersSent) {
      res.writeHead(502, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: err.message }));
    }
  });

  req.pipe(proxyReq, { end: true });
});

server.listen(PUBLIC_PORT, () => {
  console.log(`MCP Gateway Proxy listening on port ${PUBLIC_PORT} -> supergateway :${INTERNAL_PORT}`);
});
