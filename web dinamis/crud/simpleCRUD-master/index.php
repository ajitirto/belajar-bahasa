<?php 
include 'koneksi.php';
?>
<!DOCTYPE html>
<html>
<head>
	<title>SimpleCRUD</title>
</head>
<body align="center">
<h1>SimpleCrud</h1>
<?php 
//notifikasi pesan
if (!empty($_GET['pesan']) && ($_GET['pesan']=='sukses')) {
	echo "<h4>Tambah data berhasil !</h4>";
}elseif (!empty($_GET['pesan']) && ($_GET['pesan']=='hapus')) {
	echo "<h4>Hapus data berhasil !</h4>";
}elseif (!empty($_GET['pesan']) && ($_GET['pesan']=='update')) {
	echo "<h4>Update data berhasil !</h4>";
}
?>
<h4><a href="tambah.php">+ Tambah Data</a></h4>
<?php 
$query = mysql_query("select * from biodata");	
$hitung = mysql_num_rows($query);
if ($hitung>0) {	
	//jika data ada
?>
	<table border="1" cellspacing="0" cellpadding="5" align="center">
		<tr>
			<td>No.</td>
			<td>Nama</td>
			<td>Alamat</td>
			<td>Nomor telepon</td>
			<td>Email</td>
			<td>Opsi</td>
		</tr>
		<?php 
		
		$no = 1;
		while ($data=mysql_fetch_array($query)) {			
		?>
		<tr>
			<td><?php echo $no;?>. </td>
			<td><?php echo $data['nama'];?></td>
			<td><?php echo $data['alamat'];?></td>
			<td><?php echo $data['no_hp'];?></td>
			<td><?php echo $data['email'];?></td>
			<td>
				<a href="edit.php?id=<?php echo $data['kd_biodata'];?>">Edit</a> ||
				<a href="index.php?hapus=<?php echo $data['kd_biodata'];?>">Hapus</a>
			</td>
		</tr>
		<?php $no++;} ?>
	</table>
<?php 
}else{
	//jika tidak ada data
	echo "<h3>Tidak ada data </h3>";
}
?>
</body>
</html>
<?php 
//jika tombol hapus diklik
if (isset($_GET['hapus'])) {
	$kd_biodata = $_GET['hapus'];
	$hapus = mysql_query("DELETE FROM biodata WHERE kd_biodata='$kd_biodata'")or die(mysql_error());
	if ($hapus) {
		header('location:index.php?pesan=hapus');
	}
}
?>