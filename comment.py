#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
 #   <title>Reg</title>
  #  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
   #       integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    #<style>
     #   p input {
      #      width: 100%;
       # }
    #</style>
#</head>
#<body class="d-flex justify-content-center align-items-center" style="height: 100vh;">
#<form method="post" class="border w-25 p-3 rounded">
 #   <h3 class="text-center mb-2">Sign Up</h3>
 #   {% csrf_token %}
 #   {{ form.as_p }}
 #   <div class="w-100 d-flex">
  #      <button type="submit" class="btn btn-primary w-50 me-1">Sign Up</button>
   #     <a href="/" class="btn btn-danger w-50 ms-1">Back</a>
   # </div>
#</form>
#</body>
#</html>