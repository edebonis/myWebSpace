from storages.backends.s3boto3 import S3Boto3Storage
from ..settings import core_settings


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = core_settings.STATIC_ROOT
    bucket_name = 'edebonismedia'


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = core_settings.MEDIA_ROOT
    bucket_name = 'edebonismedia'
