from rest_framework import serializers

from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {"input_type":"password"}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'passwod', 'password2']
        
        extra_kwargs = {
            'password':{'write_only':True},
        }
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({"error": "Passwords must be identical!"})
        
        user = User.objects.filter(email = self.validated_data['email'])
        if user.exists():
            raise serializers.ValidationError({"error":"This email is already taken!"})
        
        account = User(username=self.validated_data["username"], email=self.validated_data["email"])
        account.set_password(password)
        account.save()
        return account