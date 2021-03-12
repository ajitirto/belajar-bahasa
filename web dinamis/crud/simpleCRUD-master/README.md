# simpleCRUD
SimpleCRUD adalah aplikasi Create, Read, Update dan Delete data sederhana yang dibangun dengan bahasa PHP.

Fitur :<br>
+CRUD (Create, Read, Update dan Delete data)<br>
+notifikasi, pesan ketika sukses tambah data, sukses update data, maupun hapus data.<br>

Cara setting <br>
+buat folder baru di htdocs misal simpleCRUD<br>
+extract file dalam master kedalam folder yang telah dibuat<br>
+buka phpmyadmin dan buat database baru dengan nama 'db_simplecrud'<br>
+import file db_simplecrud.sql ke database<br>
+buka file koneksi dengan notepad dan edit seperti berikut :<br>
  $host = 'localhost';<br>
  $user = 'root'; //username database di phpmyadmin<br>
  $pass = ''; //password database di phpmyadmin defaultnya kosong => ''<br>
  $db = 'db_simplecrud'; //nama database di phpmyadmin<br>
  
