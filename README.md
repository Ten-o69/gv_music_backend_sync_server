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

4. **Create and configure the `.env.dev` file:**

   In the project root, create a file named `.env.dev` with the following content:

   ```env
   # database
   DATABASE_URL=pymysql://user:password@ip:port/db
   DATABASE_LOG=False

   # paths
   DIR_DATA=path/to/dir/

   # log
   LOG_LEVEL=0
   ```

5. **Set environment variable to specify the mode:**

   ```bash
   export ENV_MODE=dev  # On Windows: set ENV_MODE=dev
   ```

## 🛠️ Usage

Run the synchronization server:

```bash
python main.py
```

Or you can build a docker image and run the container:
```bash
docker build -t my_image .
docker run -e ENV=prod --env-file .env.prod my_image
```

The server will start and perform synchronization based on the specified `ENV_MODE`.

- In **development mode (`dev`)**: Synchronization occurs every 10 seconds.
- In **production mode (`prod`)**: Synchronization occurs every 60 seconds.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.