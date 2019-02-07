$(document).ready(function(){
  updateProfile();
  getProfile();
  $("#edit-profile").click(function(){

  });

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
        console.log("CHAMOU POPULATE");
        populatePostCard(response.user.posts);
        //console.log(response.user.posts.author);

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

function populatePostCard(data){
    $.each(data, function(key, value){
        let card = createPostCard(value.body, value.title, value.post_date);
        $("#posts").append(card);
    });
}

function createPostCard(body, title, post_date){
    var divCard = document.createElement("div");
    var divSegment = document.createElement("div");
    var divContent = document.createElement("div");
    var imgPost = document.createElement("img");
    var h3Title = document.createElement("h3");

    $(divCard).attr("class", "card");
    $(divSegment).attr("class", "ui left piled segment");
    $(imgPost).attr("class", "ui tiny left floated image");
    $(h3Title).attr("class", "ui header text-center");
    $(divContent).attr("class", "floated right text-center description");
    $(imgPost).attr("src", "../static/img/noavatar.png");

    $(h3Title).html(title);
    $(divContent).html(body);

    divCard.appendChild(divSegment);
    divSegment.appendChild(imgPost);
    divSegment.appendChild(h3Title);
    divSegment.appendChild(divContent);
    return divCard;
}
