document.getElementById('avatar').addEventListener('change', function (event) {
  const label = event.target.nextElementSibling;
  const fileName = event.target.files[0] ? event.target.files[0].name : 'Choose File';
  label.textContent = fileName;

  const preview = document.getElementById('avatar-preview');
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      preview.src = e.target.result;
      preview.style.display = 'inline';
    };
    reader.readAsDataURL(file);
  } else {
    preview.src = '#';
    preview.style.display = 'none';
  }
});
