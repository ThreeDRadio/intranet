import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';

moduleForComponent('playlist-edit-tablerow', 'Integration | Component | playlist edit tablerow', {
  integration: true
});

test('it renders', function(assert) {
  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });

  this.render(hbs`{{playlist-edit-tablerow}}`);

  assert.equal(this.$().text().trim(), '');

  // Template block usage:
  this.render(hbs`
    {{#playlist-edit-tablerow}}
      template block text
    {{/playlist-edit-tablerow}}
  `);

  assert.equal(this.$().text().trim(), 'template block text');
});
