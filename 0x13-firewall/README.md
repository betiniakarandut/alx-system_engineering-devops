# 0x13. Firewall

## Description :house:
In this project, I began to put in place security measures to ensure that my server(s) filter out both incoming and outgoing network traffic appropriately through firewall rules.

## Tasks :pencil:
| task | Description |
|------|-------------|
|0-block_all_incoming_traffic_but | Configure ufw so that it blocks all incoming traffic, except the following TCP ports:<br>22 (SSH)<br>443 (HTTPS SSL)<br>80 (HTTP)|
|100-port_forwarding | Requirements:<br>Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.<br>Your answer file should be a copy of the ufw configuration file that you modified to make this happen|
