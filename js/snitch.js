var canvas = "";
var context ="";

document.getElementById('open_cam_button').addEventListener("click", function() {
	// Grab elements, create settings, etc.
    var video = document.getElementById('video');
    // Get access to the camera!
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        // Not adding `{ audio: true }` since we only want video now
        navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
            video.src = window.URL.createObjectURL(stream);
            video.play();

        });
    }
    // Elements for taking the snapshot
     canvas = document.getElementById('canvas');
     context = canvas.getContext('2d');


    document.getElementById("snap").addEventListener("click", function() {
        context.drawImage(video, 0, 0, 200, 200);
        video.pause();
        video.src="";



    });


});

document.getElementById('send_img').addEventListener("click", function(){
    var dataUrl = canvas.toDataURL();
    console.log(dataUrl);
    $.ajax({
        type:"POST",
        url:"/image",
        data: {
            imgBase64: dataUrl
       }
    }).done(function(o){
        console.log('saved')

    })

});

