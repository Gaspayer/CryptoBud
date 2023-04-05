document.getElementById('image').addEventListener('change', function (event) {
  const label = event.target.nextElementSibling;
  const fileCount = event.target.files.length;
  const fileName = fileCount > 0 ? `${fileCount} files selected` : 'Choose Files';
  label.textContent = fileName;

  const previewContainer = document.getElementById('image-previews');
  previewContainer.innerHTML = ''; // Clear previous previews

  for (let i = 0; i < fileCount; i++) {
    const file = event.target.files[i];
    if (file) {
      const img = document.createElement('img');
      img.style.maxWidth = '100px';
      img.style.maxHeight = '100px';
      img.style.marginRight = '10px';
      img.style.marginBottom = '10px';
      previewContainer.appendChild(img);

      const reader = new FileReader();
      reader.onload = function (e) {
        img.src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  }
});
