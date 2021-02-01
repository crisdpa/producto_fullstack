import axios from 'axios';

let mapQuestKey = '';
const addressStored = {};

if (process && process.env) {
  if (process.env.MAPQUEST_KEY) {
    mapQuestKey = process.env.MAPQUEST_KEY;
  }
}

/**
 * Return a HTML template
 */
const getTemplate = (address) => {
  return `
    <div class="widget">
      <p>${address ? address : 'cargando dirección...' }</p> 
    </div>
  `;  
};

/**
 * Format a location object obtained from Mapquest request
 */
const formatAddress = (data) => {
  let address = '';
  try {
    const addressDetails = data.results[0].locations[0];
    address = `
      ${addressDetails.street}, ${addressDetails.adminArea5}<br>
      ${addressDetails.adminArea3}, ${addressDetails.adminArea1}<br>
      ${addressDetails.postalCode}
    `;
  }
  catch (e) {
    //pass
  }
  return address;
};

/**
 * Get a saved address locally
 */
const getStoredAddress = (lat, lng) => {
  if (addressStored[`${lat}${lng}`]) {
    return addressStored[`${lat}${lng}`]
  }
  return false;
};

/**
 * Save a new address locally
 */
const setStoreAddress = (lat, lng, address) => {
  addressStored[`${lat}${lng}`] = address;
};

/**
 * Get the address of a given latitude and longitude
 * If address is found, it's store locally for future requests
 */
const getLocationAddress = (lat, lng) => {
  const serviceEndpointParams = [
    `key=${mapQuestKey}`,
    `location=${lat},${lng}`,
    'outFormat=json',
    'thumbMaps=false'
  ];
  let serviceEndpoint = 'http://open.mapquestapi.com/geocoding/v1/reverse';
  serviceEndpoint += '?' + serviceEndpointParams.join('&');

  return new Promise((resolve, reject) => {
    const addressStored = getStoredAddress(lat, lng);
    if (addressStored !== false) {
      resolve(addressStored);
    } else {
      axios.get(serviceEndpoint)
      .then((response) => {
        const addressFormated = formatAddress(response.data);
        setStoreAddress(lat, lng, addressFormated);
        resolve(addressFormated);
      })
      .catch((error) => {
        reject(error);
      })
    }
  });
};

/**
 * Get address and load it in a Popup marker
 */
export const setContent = (e) => {
  const { lat, lng } = e.popup.getLatLng();
  let template = getTemplate('');
  let address = '';
  e.popup.setContent(template);

  getLocationAddress(lat, lng)
  .then((response) => {
      address = response;
  })
  .catch((error) => {
      address = 'No se pudo obtener la dirección';
  })
  .finally(() => {
      template = getTemplate(address);
      e.popup.setContent(template);
  });
};