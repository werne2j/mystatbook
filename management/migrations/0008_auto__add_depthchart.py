# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DepthChart'
        db.create_table(u'management_depthchart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['management.Team'])),
            ('catch1', self.gf('django.db.models.fields.CharField')(default='Catcher', max_length=100)),
            ('catch2', self.gf('django.db.models.fields.CharField')(default='Catcher', max_length=100)),
            ('first1', self.gf('django.db.models.fields.CharField')(default='First Base', max_length=100)),
            ('first2', self.gf('django.db.models.fields.CharField')(default='First Base', max_length=100)),
            ('second1', self.gf('django.db.models.fields.CharField')(default='Second Base', max_length=100)),
            ('second2', self.gf('django.db.models.fields.CharField')(default='Second Base', max_length=100)),
            ('short1', self.gf('django.db.models.fields.CharField')(default='Shortstop', max_length=100)),
            ('short2', self.gf('django.db.models.fields.CharField')(default='Shortstop', max_length=100)),
            ('third1', self.gf('django.db.models.fields.CharField')(default='Third Base', max_length=100)),
            ('third2', self.gf('django.db.models.fields.CharField')(default='Third Base', max_length=100)),
            ('left1', self.gf('django.db.models.fields.CharField')(default='Left Field', max_length=100)),
            ('left2', self.gf('django.db.models.fields.CharField')(default='Left Field', max_length=100)),
            ('center1', self.gf('django.db.models.fields.CharField')(default='Center Field', max_length=100)),
            ('center2', self.gf('django.db.models.fields.CharField')(default='Center Field', max_length=100)),
            ('right1', self.gf('django.db.models.fields.CharField')(default='Right Field', max_length=100)),
            ('right2', self.gf('django.db.models.fields.CharField')(default='Right Field', max_length=100)),
            ('starter1', self.gf('django.db.models.fields.CharField')(default='Starting Pitcher', max_length=100)),
            ('starter2', self.gf('django.db.models.fields.CharField')(default='Starting Pitcher', max_length=100)),
            ('starter3', self.gf('django.db.models.fields.CharField')(default='Starting Pitcher', max_length=100)),
            ('starter4', self.gf('django.db.models.fields.CharField')(default='Starting Pitcher', max_length=100)),
            ('relief1', self.gf('django.db.models.fields.CharField')(default='Relief Pitcher', max_length=100)),
            ('relief2', self.gf('django.db.models.fields.CharField')(default='Relief Pitcher', max_length=100)),
            ('relief3', self.gf('django.db.models.fields.CharField')(default='Relief Pitcher', max_length=100)),
            ('relief4', self.gf('django.db.models.fields.CharField')(default='Relief Pitcher', max_length=100)),
            ('dh', self.gf('django.db.models.fields.CharField')(default='Designated Hitter', max_length=100)),
        ))
        db.send_create_signal(u'management', ['DepthChart'])


    def backwards(self, orm):
        # Deleting model 'DepthChart'
        db.delete_table(u'management_depthchart')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'management.depthchart': {
            'Meta': {'object_name': 'DepthChart'},
            'catch1': ('django.db.models.fields.CharField', [], {'default': "'Catcher'", 'max_length': '100'}),
            'catch2': ('django.db.models.fields.CharField', [], {'default': "'Catcher'", 'max_length': '100'}),
            'center1': ('django.db.models.fields.CharField', [], {'default': "'Center Field'", 'max_length': '100'}),
            'center2': ('django.db.models.fields.CharField', [], {'default': "'Center Field'", 'max_length': '100'}),
            'dh': ('django.db.models.fields.CharField', [], {'default': "'Designated Hitter'", 'max_length': '100'}),
            'first1': ('django.db.models.fields.CharField', [], {'default': "'First Base'", 'max_length': '100'}),
            'first2': ('django.db.models.fields.CharField', [], {'default': "'First Base'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left1': ('django.db.models.fields.CharField', [], {'default': "'Left Field'", 'max_length': '100'}),
            'left2': ('django.db.models.fields.CharField', [], {'default': "'Left Field'", 'max_length': '100'}),
            'relief1': ('django.db.models.fields.CharField', [], {'default': "'Relief Pitcher'", 'max_length': '100'}),
            'relief2': ('django.db.models.fields.CharField', [], {'default': "'Relief Pitcher'", 'max_length': '100'}),
            'relief3': ('django.db.models.fields.CharField', [], {'default': "'Relief Pitcher'", 'max_length': '100'}),
            'relief4': ('django.db.models.fields.CharField', [], {'default': "'Relief Pitcher'", 'max_length': '100'}),
            'right1': ('django.db.models.fields.CharField', [], {'default': "'Right Field'", 'max_length': '100'}),
            'right2': ('django.db.models.fields.CharField', [], {'default': "'Right Field'", 'max_length': '100'}),
            'second1': ('django.db.models.fields.CharField', [], {'default': "'Second Base'", 'max_length': '100'}),
            'second2': ('django.db.models.fields.CharField', [], {'default': "'Second Base'", 'max_length': '100'}),
            'short1': ('django.db.models.fields.CharField', [], {'default': "'Shortstop'", 'max_length': '100'}),
            'short2': ('django.db.models.fields.CharField', [], {'default': "'Shortstop'", 'max_length': '100'}),
            'starter1': ('django.db.models.fields.CharField', [], {'default': "'Starting Pitcher'", 'max_length': '100'}),
            'starter2': ('django.db.models.fields.CharField', [], {'default': "'Starting Pitcher'", 'max_length': '100'}),
            'starter3': ('django.db.models.fields.CharField', [], {'default': "'Starting Pitcher'", 'max_length': '100'}),
            'starter4': ('django.db.models.fields.CharField', [], {'default': "'Starting Pitcher'", 'max_length': '100'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Team']"}),
            'third1': ('django.db.models.fields.CharField', [], {'default': "'Third Base'", 'max_length': '100'}),
            'third2': ('django.db.models.fields.CharField', [], {'default': "'Third Base'", 'max_length': '100'})
        },
        u'management.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'doubleheader': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'opponent': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Team']"}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'management.player': {
            'Meta': {'object_name': 'Player'},
            'class_standing': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hits': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['management.Position']", 'symmetrical': 'False'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Team']"}),
            'throws': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        u'management.playerstats': {
            'Meta': {'object_name': 'PlayerStats'},
            'at_bats': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'earned_runs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['management.Game']"}),
            'hit_by_pitch': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hits': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hits_allowed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hr': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innings': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'loss': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'playerstats'", 'to': u"orm['management.Player']"}),
            'rbi': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'runs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'runs_allowed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strikeout_amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strikeouts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'walks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'walks_allowed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wild_pitches': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'win': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'management.position': {
            'Meta': {'object_name': 'Position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'management.team': {
            'Meta': {'object_name': 'Team'},
            'coach': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['management']