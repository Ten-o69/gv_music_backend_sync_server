# 🎵 GV Music Backend Sync Server

Sync server that is used in the main project [gv_music_backend](https://github.com/Ten-o69/gv_music_backend).
Very simple implementation of synchronisation of paths within the database and by actual paths in the file system.

## 🚀 Features

- Periodic synchronization of music tracks and cover images from the database to the local file system.
- Automatic removal of orphaned files not present in the database.

## ⚙️ Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ten-o69/gv_music_backend_sync_server.git
   cd gv_music_backend_sync_server
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**

   Set the `ENV_MODE` environment variable to specify the mode of operation:

   - `dev` for development mode (synchronizes every 10 seconds)
   - `prod` for production mode (synchronizes every 60 seconds)

   Example:

   ```bash
   export ENV_MODE=dev  # On Windows: set ENV_MODE=dev
   ```

## 🛠️ Usage

Run the synchronization server:

```bash
python main.py
```

The server will start and perform synchronization based on the specified `ENV_MODE`.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.