define([
  'pat-base',
  'mockup-patterns-structure-url/pattern-structureupdater',
], function(Base) {
  'use strict';
  var Pattern = Base.extend({
    name: 'structureupdater-sidebar',
    trigger: '.template-folder_contents',
    parser: 'mockup',
    init: function() {
      $('body').on('context-info-loaded', function(e, data) {

        // TODO: Implement

      }.bind(this));
    }
  });
  return Pattern;
});
