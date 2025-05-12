const BASE_URL = 'https://batik-backend-v2-792988373365.asia-southeast2.run.app';

const ENDPOINT = {
  predict: `${BASE_URL}/predict`,
};

class PredictAPI {
  static async predict(data) {
    const response = await fetch(ENDPOINT.predict, {
      method: 'POST',
      body: data,
      redirect: 'follow',
    });

    const contentType = response.headers.get('content-type');

    if (!response.ok) {
      // Coba ambil pesan error dari response jika ada
      let errorMessage = `HTTP error ${response.status}`;
      if (contentType && contentType.includes('application/json')) {
        const errorData = await response.json();
        errorMessage = errorData.message || errorMessage;
      }
      throw new Error(errorMessage);
    }

    const json = await response.json();
    return json;
  }
}
