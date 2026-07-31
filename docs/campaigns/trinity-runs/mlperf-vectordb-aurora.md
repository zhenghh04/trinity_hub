# MLPerf Storage vector-database benchmark: DAOS vs. Lustre on Aurora

**System:** Aurora · **Type:** Storage/ML benchmark · **Outcome:** :material-database-search: Success

## The ask

*(This campaign predates verbatim prompt logging — the request below is reconstructed from the campaign's recorded intent, not a direct quote.)*

> "Benchmark vector-database datagen and search performance on Aurora comparing the DAOS parallel filesystem against Lustre, then characterize multi-node client scaling of query throughput."

## What happened

This overnight campaign benchmarked MLPerf Storage's DISKANN vector-database workload on Aurora, comparing DAOS against Lustre storage, then scaled out across multiple client nodes. It required several infrastructure fixes along the way: filesystem configuration flags, an isolated software stack to avoid authentication errors, a small patch to capture index-type metadata, and a missing-package bug fix. A production reservation was unavailable, so the campaign ran on the standard production queue instead. The first scaling-sweep attempt failed silently due to a naming/liveness issue; the second, with fixes applied, succeeded.

## Results

- DAOS search throughput: 2,188 queries/sec vs. Lustre's 296 queries/sec (7-23x faster); p99 latency 28.4 ms (DAOS) vs. 244.4 ms (Lustre) — 10-30x lower.
- Index-build (write) phase was actually faster on Lustre (227s) than DAOS (492s) — the DAOS pool was in a degraded state during this run, a real caveat worth disclosing.
- Multi-node client aggregate throughput scaled from 1,176 to 1,989 to 2,358 queries/sec as client ranks increased, then plateaued — determined to be the ceiling of the single benchmark server, not a client/network limit.
- Recall@10 = 0.42 for the 100K-vector index.

[← Back to Trinity runs](index.md)
