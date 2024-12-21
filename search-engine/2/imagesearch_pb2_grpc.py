# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import imagesearch_pb2 as imagesearch__pb2


class ImageSearchServiceStub(object):
    """Service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchForKeyword = channel.unary_unary(
                '/imagesearch.ImageSearchService/SearchForKeyword',
                request_serializer=imagesearch__pb2.KeywordRequest.SerializeToString,
                response_deserializer=imagesearch__pb2.ImageResponse.FromString,
                )


class ImageSearchServiceServicer(object):
    """Service definition
    """

    def SearchForKeyword(self, request, context):
        """Method to search for an image based on a keyword
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageSearchServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SearchForKeyword': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchForKeyword,
                    request_deserializer=imagesearch__pb2.KeywordRequest.FromString,
                    response_serializer=imagesearch__pb2.ImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'imagesearch.ImageSearchService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageSearchService(object):
    """Service definition
    """

    @staticmethod
    def SearchForKeyword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/imagesearch.ImageSearchService/SearchForKeyword',
            imagesearch__pb2.KeywordRequest.SerializeToString,
            imagesearch__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)