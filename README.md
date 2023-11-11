# slsher

Slsher or "scaled-locality-sensitive-hash-er" is a tool for generating, comparing and clustering LSH (and a bunch of other fingerprints!) in a user friendly way.

# Roadmap
- [ ] Modular system for creating fingerprints.
- [ ] Files and fingerprints are documented in Elasticsearch.
- [ ] Files can be posted to an API for fingerprinting and documentation.
- [ ] Fingerprint generation is deferred to celery tasks (for async!)
- [ ] Fingerprint comparison implemented.
- [ ] Fingerprint comparison is also deferred to celery tasks (again, for async!)
- [ ] Fingerprint comparison results form edges on a Neo4J graph.
- [ ] UI for posting files.
- [ ] UI for comparing files.
- [ ] Files automatically compared at scale with the rest of the dataset on post.
- [ ] Files (and collections) can be tagged with labels (APTs, technologies etc).