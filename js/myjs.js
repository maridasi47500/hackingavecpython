function on() {
  document.getElementById("mid").style.display="block"
}
function off() {
  document.getElementById("mid").style.display="none"
}
function previewfile() {
  const content = document.querySelector('.content');
  const [file] = document.querySelector('input[type=file]').files;
  const reader = new FileReader();

  reader.addEventListener("load", () => {
    // this will then display a text file
    content.innerHTML = reader.result;
  }, false);

  if (file) {
    reader.readAsText(file);
  }
}
