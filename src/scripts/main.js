// Catch elements
const dropArea = document.getElementById('dropArea');
const predictForm = document.getElementById('predictForm');
const previewImg = document.getElementById('previewImg');

const waitingToPredicting = document.querySelector('.result-container #waitingToPredicting');
const loadingPredict = document.querySelector('.result-container .loading');
const predictionError = document.querySelector('.result-container #predictionError');
const result = document.querySelector('.result-container #result');

// Form data
const predictFormData = new FormData();

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach((eventName) => {
  dropArea.addEventListener(eventName, preventDefaults, false);
  document.body.addEventListener(eventName, preventDefaults, false);
});

// Prevent submitting form behaviors
['submit'].forEach((eventName) => {
  predictForm.addEventListener(eventName, preventDefaults, false);
});

// Highlight drop area when item is dragged over it
['dragenter', 'dragover'].forEach((eventName) => {
  dropArea.addEventListener(eventName, highlight, false);
});
// Remove highlight drop area when item is drag leave
['dragleave', 'drop'].forEach((eventName) => {
  dropArea.addEventListener(eventName, unhighlight, false);
});

function preventDefaults(event) {
  event.preventDefault();
  event.stopPropagation();
}

function highlight() {
  dropArea.classList.add('highlight');
}

function unhighlight() {
  dropArea.classList.remove('highlight');
}

// Handle dropped and submit files
dropArea.addEventListener('drop', dropHandler, false);
predictForm.elements.batikFile.addEventListener('change', batikFileInputHandler);
predictForm.addEventListener('submit', predictFormSubmitHandler);

function dropHandler(event) {
  const dataTransfer = event.dataTransfer;
  const files = dataTransfer.files;

  const batikImage = files[0];
  predictFormData.set('image', batikImage, batikImage.name); // ganti 'file' jadi 'image'

  previewFile(batikImage);
}

// Handle file by input element
function batikFileInputHandler(event) {
  const files = Array.from(event.target.files);

  const batikImage = files[0];
  predictFormData.set('image', batikImage, batikImage.name); // ganti 'file' jadi 'image'

  previewFile(batikImage);
}

// Handle submit form
function predictFormSubmitHandler() {
  if (!predictFormData.has('image')) {
    alert('Silakan pilih gambar batik terlebih dahulu');
    return;
  }

  uploadFile(predictFormData);
}

// Show preview after choose image
function previewFile(file) {
  const reader = new FileReader();
  reader.readAsDataURL(file);

  reader.onloadend = () => {
    previewImg.innerHTML = '';

    const img = document.createElement('img');
    img.src = reader.result;
    previewImg.appendChild(img);
  };
}

// Send image to server
async function uploadFile(formData) {
  try {
    hideElement(waitingToPredicting);
    hideElement(result);
    showElement(loadingPredict);

    const response = await PredictAPI.predict(formData);

    showPredictionResult(response);
    showElement(result);
  } catch (error) {
    console.error(error);
    predictionError.textContent = error.message;
  } finally {
    hideElement(loadingPredict);
  }
}

// Show result to user
function showPredictionResult(response) {
  const { prediction, confidence, suggestion, timestamp } = response;

  result.innerHTML = `
    <div class="response-message">
      <i class="fas fa-check"></i>
      <span class="message">Proses Prediksi Berhasil!</span>
    </div>
    <div class="prediction-result">
      <div>
        <div class="result-title">Hasil Prediksi</div>
        <div>${prediction}</div>
      </div>
      <div>
        <div class="result-title">Penjelasan Prediksi</div>
        <div>${suggestion}</div>
      </div>
      <div>
        <div class="result-title">Riwayat Prediksi</div>
        <div>${timestamp}</div>
      </div>
    </div>
  `;
}
