'use strict';

angular.module('dopemsgServices', ['ngRoute', 'ngResource'])
  .factory('Post', function($http) {
    return {
      postPhone: function(form) {
        return $http.post('/save-phone', form, {
          headers: {'Content-Type': undefined},
          transformRequest: angular.identity
        });
      }
    }
  });
