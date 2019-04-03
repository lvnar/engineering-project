'use strict';

let request = require('request')

let requestPromise = function(payload) {
  return new Promise(function (resolve, reject) {
    request(payload, function (error, response, body) {
      if (error) {
        sails.log.error(error);
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

module.exports = {
  login: function (req, res) {
    let reqData = {
      url: sails.config.env.host + '/login/',
      method: 'POST',
      form: req.allParams()
    };
    return requestPromise(reqData).then(resp => {
      req.session.token = 'Token ' + resp.key;
      let reqData2 = {
        url: sails.config.env.host + '/user/',
        method: 'GET',
        headers: {
          Authorization: req.session.token
        }
      };
      return requestPromise(reqData2);
    }).then(resp => {
      //res.location('/map');
      req.session.username = resp.username;
      return res.redirect('/map');
    }).catch(error => {
      return res.redirect('/');
    });
  },
  logout: function (req, res) {
    let reqData = {
      url: sails.config.env.host + '/logout/',
      method: 'POST',
      headers: {
        Authorization: req.session.token
      }
    };
    return requestPromise(reqData).then(resp => {
      delete req.session.token;
      req.session.destroy();
      return res.redirect('/');
    }).catch(error => {
      return res.redirect('/');
    });
  }
};
