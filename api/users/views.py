
from flask import request, jsonify
from flask.views import MethodView

from api.auth.auth_utils import token_needed
from api.users.utils import upload_profile_picture, save_profile_picture


class UserProfilePicView(MethodView):
    """Update User file."""
    decorators = [token_needed]

    def post(self, current_user):

        # receive image from user upload
        image = request.files.get("image")
        if not image:
            message = {"message": "No file uploaded"}
            return jsonify(message), 400
        try:

            # upload the image
            url = upload_profile_picture(image)
            save_profile_picture(current_user, url)

            return jsonify({"Profile Picture Url": url}), 201

        except Exception:
            error_data = {"message": "Failed to upload file to bucket"}
            return jsonify(error_data), 500


class UsersView(MethodView):
    """ View to handle user functionality."""
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
