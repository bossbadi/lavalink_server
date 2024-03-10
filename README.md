# Lavalink Server

A Lavalink server ready to be deployed to Heroku or Repl.it


## Deploy on Heroku
See the [`port80`](https://github.com/bossbadi/lavalink_server/tree/port80) branch


## Deploy on a cloud server (Ubuntu)

### Basic installation

Install dependencies
```bash
sudo apt update
sudo apt install -y git  # for cloning the repository
sudo apt install -y openjdk-13-jre  # for running Lavalink
```

Clone the repository
```bash
git clone "https://github.com/bossbadi/lavalink_server"
```

Run Lavalink
```bash
cd lavalink_server/
java -jar Lavalink.jar
```

```bash
# OR to run server in background
nohup java -jar Lavalink.jar &
```

### Advanced installation

Install dependencies
```bash
sudo apt update
sudo apt install -y git  # for cloning the repository
sudo apt install -y openjdk-13-jre  # for running Lavalink
sudo apt install -y supervisor  # for monitoring the server
```

Clone the repository
```bash
git clone "https://github.com/bossbadi/lavalink_server"
```

Create config file for Supervisor
```bash
sudo vim /etc/supervisor/conf.d/lavalink.conf
```

Paste the following content, edit the highlighted parts to match your server configuration
```conf
[program:lavalink]
directory=/home/YOUR_USERNAME/lavalink_server
command=java -jar Lavalink.jar
user=YOUR_USERNAME
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/home/YOUR_USERNAME/lavalink_server/logs/err.log
stdout_logfile=/home/YOUR_USERNAME/lavalink_server/logs/out.log
```

Restart Supervisor to start Lavalink
```bash
sudo supervisorctl reload
```

### Connecting to your server

- **host:** your server's IP address (e.g `1.2.3.4`)
- **port:** `2333`
- **password:** `youshallnotpass`
- **region:** `en` (doesn't matter)
- **name:** `node-1` (doesn't matter)

You can fork the repository and change `application.yml` to your liking.

### Troubleshooting

**Q:** Lavalink server is running but bot can't connect \
**A:** The firewall may be blocking the port. Use Firewalld to open the port. For some cloud service providers, you may also need to manually add the port to the allowed ingress rules.
```bash
sudo apt install -y firewalld  # Install Firewalld
sudo firewall-cmd --permanent --add-port=2333/tcp  # Open the port
sudo firewall-cmd --reload  # Reload changes
```
