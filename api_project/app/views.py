from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Category, Article, Comment

class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        categories_list = []
        for category in categories:
            categories_list.append({
                "pk": category.pk,
                "name": category.name
            })
        return Response(categories_list)

    def post(self, request: Request):
        try:
            category = Category.objects.create(
                name=request.data["name"]
            )
            return Response(model_to_dict(category))
        except Exception as e:
            return Response(str(e), status=404)

class CategoryDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            return Response(model_to_dict(category))
        except Exception as e:
            return Response(str(e), status=404)

class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        articles_list = []
        for article in articles:
            articles_list.append({
                "sarlavha": article.sarlavha,
                "tarkib": article.tarkib,
                "chop_etilgan_sana": article.chop_etilgan_sana,
                "category": str(article.category),
                "korishlar_soni": article.korishlar_soni,
                "muallif": article.muallif,
            })
        return Response(articles_list)

    def post(self, request: Request):
        try:
            article = Article.objects.create(
                sarlavha=request.data["sarlavha"],
                tarkib=request.data["tarkib"],
                chop_etilgan_sana=request.data["chop_etilgan_sana"],
                category=request.data["category"],
                korishlar_soni=request.data["korishlar_soni"],
                muallif=request.data["muallif"],
            )
            return Response(model_to_dict(article))
        except Exception as e:
            return Response(str(e), status=404)

class ArticleDetailView(APIView):
    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            return Response(model_to_dict(article))
        except Exception as e:
            return Response(str(e), status=404)

class CommentAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        comment_list = []
        for comment in comments:
            comment_list.append({
                "article": str(comment.article),
                "user": str(comment.user),
                "email": comment.email,
                "sharh_matni": comment.sharh_matni,
                "chop_etilgan_sana": comment.chop_etilgan_sana
            })
        return Response(comment_list)

    def post(self, request: Request):
        try:
            comment = Comment.objects.create(
                article=request.data["article"],
                user=request.data["user"],
                email=request.data["email"],
                sharh_matni=request.data["sharh_matni"],
                chop_etilgan_sana=request.data["chop_etilgan_sana"],
            )
            return Response(model_to_dict(comment))
        except Exception as e:
            return Response(str(e), status=404)

class CommentDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            return Response(model_to_dict(comment))
        except Exception as e:
            return Response(str(e), status=404)