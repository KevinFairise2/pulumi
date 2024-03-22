// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.DocumentDB.Outputs
{

    [OutputType]
    public sealed class SqlContainerGetPropertiesResponseResource
    {
        /// <summary>
        /// The configuration of the indexing policy. By default, the indexing is automatic for all document paths within the container
        /// </summary>
        public readonly Outputs.IndexingPolicyResponse? IndexingPolicy;

        [OutputConstructor]
        private SqlContainerGetPropertiesResponseResource(Outputs.IndexingPolicyResponse? indexingPolicy)
        {
            IndexingPolicy = indexingPolicy;
        }
    }
}