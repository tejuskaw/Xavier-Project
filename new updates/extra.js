export function fileChange(e) {
  var fileInput = e;
  var file = fileInput.files[0];
  var textType = /text.*/;
  var filename = file.name;
  if (file.type.match(textType)) {
    var reader = new FileReader();

    reader.onload = function (e) {
      console.log(filename);
      var content = reader.result;
      //Here the content has been read successfuly
      document.querySelector(".ql-editor").innerText = content;
      document.querySelector("#title").value = filename;
      //toaster("Contents set from <i>" + filename + "</i>");
    };

    reader.readAsText(file);
  }
}

export function post(e) {
  setTimeout(function () {
    e.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
  }, 1000);
}
