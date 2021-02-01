import axios from 'axios';

axios.defaults.headers.common.Accept = 'application/json';

const fetch = (endpoint) => {
return axios
    .get(endpoint)
    .then((res) => res)
    .catch((err) => {
    console.error(
        'Error catch in Apiutils at fetch method. It will be thrown...');
    throw err;
    });
}

export const getPoints = () => {
    const query = 'http://0.0.0.0:8080/api/v1/location';
    return fetch(query)
      .then( res => {
        const data = [];
        res.data.rows.forEach(location => {
            data.push({
                lat: location.coordinates[0],
                lng: location.coordinates[1]
            })
        });
        return data;
      });
  };