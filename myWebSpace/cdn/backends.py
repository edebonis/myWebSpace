from storages.backends.s3boto3 import S3Boto3Storage
from myWebSpace.settings import STATIC_ROOT, MEDIA_ROOT


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = STATIC_ROOT
    bucket_name = 'edebonismedia'


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = MEDIA_ROOT
    bucket_name = 'edebonismedia'
