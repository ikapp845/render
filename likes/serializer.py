from rest_framework import serializers
from .models import Like
from group.serializers import ProfileSerializer



class LikeSerializer(serializers.ModelSerializer):
  question = serializers.SerializerMethodField("get_question")
  from_username = serializers.SerializerMethodField("get_fromuser")
  from_gender = serializers.SerializerMethodField("get_fromgender")

  class Meta:
    model = Like
    exclude = ["user_from","user_to"]

  def get_question(self,like):
    question = like.question
    return question.question

  def get_fromuser(self,like):
    user_to = like.user_to
    user_from = like.user_from
    print(user_from.paid)
    if user_to.paid == "True":
      if user_from.paid == "True":
        return "From user paid"
      else: 
        serializer = ProfileSerializer(user_from,many = False )
        return serializer.data
    else:
      return "To user not paid"

  def get_fromgender(self,like):
    user_from = like.user_from
    return user_from.gender
      


