$(document).ready(function(){
  getProfile();

  $("#uploadAvatar").change(function(){
		var reader = new FileReader();
		reader.readAsDataURL($("#uploadAvatar")[0].files[0]);

		reader.onload = function(event){
			$("#previewAvatar").attr('src', event.target.result);
		};
	});
});

function updateProfile(){
  $("#update-profile").submit(function(e){

    var formData = new FormData($(this)[0]);
    var url = "../settings/edit_profile";

    $.ajax({
      type: "POST",
      url: url,
      data: formData,
      success: function(response){
        console.log(response)
      },
      cache: false,
      contentType: false,
      processData: false
    });
    e.preventDefault();
  });
}

function getProfile(){

  $.ajax({
	    type: 'GET',
	    url: "../settings/get_profile",
	    dataType: 'json',
	    contentType: 'application/json; charset=utf-8',
	    success: function(user){
	    	console.log(user);

        $("#first_name").val(user.firstName);
        $("#last_name").val(user.lastName);
        $("#about_me").val(user.aboutMe);
        $("#previewAvatar").attr('src', user.avatar);
	    },
	    error: function(){
	    	$(this).html("error!");
	    }
	});
}

function updatePassword(){
  $("#update-password").submit(function(e){

    let data = {};
    let form = this;

    data["old_password"] = $("#old_password").val();

    let url = "../settings/update_password";
    alert(data);
    $.ajax({
      type: "POST",
      url: url,
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
      data: JSON.stringify(data),
      success: function(response){
        let obj = JSON.parse(response);
        console.log(obj.message);
      },
    });

    e.preventDefault();
  });
}
