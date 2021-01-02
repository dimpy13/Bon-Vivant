<?php

header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once './config.php';

$response = array();
 
if (isset($_POST["id"])) {

  $username = trim($_POST["username"]);
  $recipeTitle = trim($_POST["recipeTitle"]);
  $category = trim($_POST["category"]);
  $serving = trim($_POST["serving"]);
  $cookTime = trim($_POST["cookTime"]);
  $ingredientList = $_POST["ingredientList"];
  $directions = $_POST["directions"];

  
  $sql = "SELECT id AS id from tbl_users where email = :username";
  try {
    $stmt = $DB->prepare($sql);
    $stmt->bindValue(":username", $username);
    $stmt->execute();
    $result = $stmt->fetchAll();
    $id = $result[0]["id"];
    if ($result[0]["id"] > 0) {
      $sql = "INSERT INTO `uploadR` (`id`, `recipeTitle`, `category`, `serving`, `cookTime`, `ingredientList`, `directions`) VALUES " . "( :id, :recipeTitle, :category, :serving, :cookTime, :ingredientList, :directions)";
      $stmt = $DB->prepare($sql);
      $stmt->bindValue(":id", $id);
      $stmt->bindValue(":recipeTitle", $recipeTitle);
      $stmt->bindValue(":category", $category);
	  $stmt->bindValue(":serving", $serving);
      $stmt->bindValue(":cookTime", $cookTime);
      $stmt->bindValue(":ingredientList", $ingredientList);
	  $stmt->bindValue(":directions", $directions);
      $stmt->execute();
      $result = $stmt->rowCount();
      
		if ($result > 0) {
		$msg = "Upload successful";
		$msgType = "warning";
		} 
	
		else {
        $msg = "Failed to upload";
        $msgType = "warning";
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
 




