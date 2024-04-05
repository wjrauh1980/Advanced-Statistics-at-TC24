Test

<details>
  <summary>Click to toggle video</summary>
  <div id="video-container">
    <video controls id="my-video">
      <source src="[https://raw.githubusercontent.com/your_username/your_repository/branch/path/to/your/video.mp4](https://github.com/wjrauh1980/Advanced-Statistics-at-TC24/blob/main/Problem2_Videos/1%20-%20Connect%20to%20data.mp4)" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <button onclick="toggleVideo()">Toggle Video</button>
</details>

<script>
  function toggleVideo() {
    var video = document.getElementById("my-video");
    var videoContainer = document.getElementById("video-container");
    if (videoContainer.style.display === "none") {
      videoContainer.style.display = "block";
      video.play();
    } else {
      videoContainer.style.display = "none";
      video.pause();
    }
  }
</script>
