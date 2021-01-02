<?php

header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once './config.php';

$response = array();
 
if (isset($_POST["id"])) {

  $username = trim($_POST["username"]);

  $sql = "SELECT id AS id from tbl_users where email = :username";
  try {
    $stmt = $DB->prepare($sql);
    $stmt->bindValue(":username", $username);
    $stmt->execute();
    $result = $stmt->fetchAll();
    $id = $result[0]["id"];
	
    if ($result[0]["id"] > 0) {
      $sql = "SELECT * from uploadR where id = :id";
      $stmt = $DB->prepare($sql);
      $stmt->bindValue(":id", $id);
      $stmt->execute();
      $result = $stmt->fetchAll();
      
		if ($result > 0) {
		echo json_encode($reset);
		} 
	
		else {
        $msg = "Failed to upload";
        $msgType = "warning";
		echo json_encode($msgType);
        }
    }
	
	else{
	$result['msg']='0';
	echo json_encode($result["msg"]);
	}
		
  } catch (Exception $ex) {
    echo $ex->getMessage();
  }
  


}

?>
 




