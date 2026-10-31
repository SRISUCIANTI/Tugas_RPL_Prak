import hashlib
from config.database import Database

class UserModel:
    def __init__(self):
        # Memanggil koneksi melalui objek Database
        db = Database()
        self.conn = db.get_connection()

    def register_user(self, username, password, role):
        # Mengubah password menjadi hash SHA-256
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        if not self.conn:
            print("Koneksi database belum terhubung!")
            return False

        cursor = self.conn.cursor()
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (username, hashed_password, role))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error registrasi: {e}")
            return False
        finally:
            cursor.close()