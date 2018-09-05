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
