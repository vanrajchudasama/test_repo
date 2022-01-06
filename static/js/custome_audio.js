
$(document).ready(function(){
$("#mai_div").on('mouseover','.col-4', function(current) {
    $("audio").each(function(e) {
        if (e !== current.currentTarget) {
            $(this)[0].pause();
        }
    });
    $(this).children().find('audio')[0].play();
	
	
 });
});

var audio = document.createElement("audio");
audio.addEventListener('ended', function(){
    alert('done');
    });
 $("#searchResult").on('click','div.ringtone-player div.play-btn i.fa-play-circle', function(current) {

	$(this).parent().find(".fa-play-circle").css("display", "none");
        $(this).parent().find(".fa-snowflake-o").css("display", "inline-block");
        $(".fa-play-circle").not(this).parent().find(".fa-snowflake-o").css("display", "none");
        $(".fa-play-circle").not(this).parent().find(".fa-play-circle").css("display", "inline-block");

        // ADD / REMOVE CLASS
        $(this).parent().parent().addClass("isPlaying");
        $(".fa-play-circle").not(this).parent().parent().removeClass("isPlaying");
        // ani
        $(this).parent().parent().find(".beat_animation ul li").css("animation-play-state", "running").css("opacity", "1");
        $(".fa-play-circle").not(this).parent().parent().find(".beat_animation ul li").css("animation-play-state", "paused").css("opacity", ".1");

        // PASUE CURRENT AUDIO TRACK WHEN PLAY NEXT/PREV AUDIO TRACK
        $("audio").each(function(e) {
            if (e !== current.currentTarget) {
                $(this)[0].pause();
            }
        });

        // PLAY CURRENT AUDIO TRACK 
        $(this).parent().parent().find(".track audio")[0].play();
	alert('play now');
 });