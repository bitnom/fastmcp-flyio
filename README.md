change app name in fly.toml and issue `fly launch` and `fly logs` to monitor.

Attempting to use this MCP results in errors.

roocode:

```json
{
  "mcpServers": {
    "test-mcp": {
      "url": "https://flymcp.fly.dev/mcp",
      "timeout": 60,
      "disabled": false,
      "alwaysAllow": []
    }
}
```

fly logs (attempted with and without trailing-slash in mcp URL):

```
2025-05-14T16:35:44Z app[d8dd76ea161538] atl [info]INFO:     172.16.21.106:52416 - "GET /mcp HTTP/1.1" 307 Temporary Redirect
2025-05-14T16:35:44Z app[d8dd76ea161538] atl [info]INFO:     172.16.21.106:52424 - "GET /mcp/ HTTP/1.1" 400 Bad Request
2025-05-14T16:35:56Z app[d8dd76ea161538] atl [info]INFO:     172.16.21.106:34906 - "GET /mcp/ HTTP/1.1" 400 Bad Request
```