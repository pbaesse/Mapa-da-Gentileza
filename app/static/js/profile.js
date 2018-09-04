$(document).ready(function(){
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
