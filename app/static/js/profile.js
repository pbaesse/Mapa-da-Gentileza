$(document).ready(function(){
  updateProfile();
  $("#edit-profile").click(function(){
    //chamara a função getProfile() e popular o form do modal
    // para usuários atualizarem o perfil.
    getProfile();
    UIkit.modal("#my-id").show();

  })

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
    var url = "../users/settings/edit_profile";

    $.ajax({
      type: "POST",
      url: url,
      data: formData,
      async: true,
      success: function(response){
        console.log(response);
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
	    url: "../users/settings/get_profile",
	    dataType: 'json',
	    contentType: 'application/json; charset=utf-8',
	    success: function(response){
        console.log(response);
        console.log(response.user.posts.author);

        $("#username").val(response.user.username);
        $("#first_name").val(response.user.first_name);
        $("#last_name").val(response.user.last_name);
        $("#status").val(response.user.status);
        $("#phone").val(response.user.phone);
        $("#about_me").val(response.user.about_me);
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

    let url = "../users/settings/update_password";
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
