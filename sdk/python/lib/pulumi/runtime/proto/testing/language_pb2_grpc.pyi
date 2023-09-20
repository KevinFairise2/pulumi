"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2016-2023, Pulumi Corporation.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import abc
import grpc
import pulumi.testing.language_pb2

class LanguageTestStub:
    """LanguageTest is the interface to the pulumi language test framework. This is _highly_ experimental and
    currently subject to breaking changes without warning.
    """

    def __init__(self, channel: grpc.Channel) -> None: ...
    GetLanguageTests: grpc.UnaryUnaryMultiCallable[
        pulumi.testing.language_pb2.GetLanguageTestsRequest,
        pulumi.testing.language_pb2.GetLanguageTestsResponse,
    ]
    """GetLanguageTests returns a list of all the language tests."""
    PrepareLanguageTests: grpc.UnaryUnaryMultiCallable[
        pulumi.testing.language_pb2.PrepareLanguageTestsRequest,
        pulumi.testing.language_pb2.PrepareLanguageTestsResponse,
    ]
    """PrepareLanguageTests prepares the engine to run language tests. It sets up a stable artifacts folder
    (which should be .gitignore'd) and fills it with the core SDK artifact.
    """
    RunLanguageTest: grpc.UnaryUnaryMultiCallable[
        pulumi.testing.language_pb2.RunLanguageTestRequest,
        pulumi.testing.language_pb2.RunLanguageTestResponse,
    ]
    """RunLanguageTest runs a single test of the language plugin."""

class LanguageTestServicer(metaclass=abc.ABCMeta):
    """LanguageTest is the interface to the pulumi language test framework. This is _highly_ experimental and
    currently subject to breaking changes without warning.
    """

    @abc.abstractmethod
    def GetLanguageTests(
        self,
        request: pulumi.testing.language_pb2.GetLanguageTestsRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.testing.language_pb2.GetLanguageTestsResponse:
        """GetLanguageTests returns a list of all the language tests."""
    @abc.abstractmethod
    def PrepareLanguageTests(
        self,
        request: pulumi.testing.language_pb2.PrepareLanguageTestsRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.testing.language_pb2.PrepareLanguageTestsResponse:
        """PrepareLanguageTests prepares the engine to run language tests. It sets up a stable artifacts folder
        (which should be .gitignore'd) and fills it with the core SDK artifact.
        """
    @abc.abstractmethod
    def RunLanguageTest(
        self,
        request: pulumi.testing.language_pb2.RunLanguageTestRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.testing.language_pb2.RunLanguageTestResponse:
        """RunLanguageTest runs a single test of the language plugin."""

def add_LanguageTestServicer_to_server(servicer: LanguageTestServicer, server: grpc.Server) -> None: ...