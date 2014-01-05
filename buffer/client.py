from .utils import api_endpoint, args_to_kwargs, TYPES

class BufferClient(object):
    
    def __init__(self, access_token):
        self.access_token = access_token

    #
    # User details
    #
    @api_endpoint(TYPES['GET'], 'user.json')
    def user(self, data):
        pass

    #
    # Profiles details
    #
    @api_endpoint(TYPES['GET'], 'profiles.json')
    def profiles(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['GET'], 'profiles/%(id)s.json')
    def profile(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['GET'], 'profiles/%(id)s/schedules.json')
    def schedules(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['POST'], 'profiles/%(id)s/schedules/update.json')
    def update_schedules(self, data):
        pass

    #
    # Updates details 
    #
    @args_to_kwargs('id')
    @api_endpoint(TYPES['GET'], 'updates/%(id)s.json')
    def updates(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['GET'], 'profiles/%(id)s/updates/pending.json')
    def pending_updates(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['GET'], 'profiles/%(id)s/updates/sent.json')
    def sent_updates(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['GET'], 'updates/%(id)s/interactions.json')
    def interactions(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['POST'], 'profiles/%(id)s/updates/reorder.json')
    def reorder_updates(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['POST'], 'profiles/%(id)s/updates/shuffle.json')
    def shuffle_updates(self, data):
        pass

    @api_endpoint(TYPES['POST'], 'updates/create.json')
    def create_update(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['POST'], 'updates/%(id)s/update.json')
    def update_update(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['POST'], 'updates/%(id)s/share.json')
    def share_update(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['POST'], 'updates/%(id)s/destroy.json')
    def destroy_update(self, data):
        pass

    @args_to_kwargs('id')
    @api_endpoint(TYPES['POST'], 'updates/%(id)s/move_to_top.json')
    def next_update(self, data):
        pass

    #
    # Links details
    #
    @api_endpoint(TYPES['GET'], 'links/shares.json')
    def link_shares(self, data):
        pass

    #
    # Information/Configuration
    #
    @api_endpoint(TYPES['GET'], 'info/configuration.json')
    def configuration(self, data):
        pass
