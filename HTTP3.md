# Gemma Porrill HTTP3 assignment 
## When did it change over?
- 2022
## What is HTTP3?
- HTTP3 started as an experiment with QUIC.
- Stands for Quick UDP Internet Connections
## Why was there the change from HTTP2 to HTTP3?
- The main reason is changing from TCP to QUIC
- It improves latency and connection establish times
- Introduces built-in encrytion whihc makes it more secure by default
- There is also an improvement of handling packet losses
  - Helps users on unreliable networks or those experiencing high latency
  - loss of packets on one stream does not impact the other streams
  - if an error occurs, only the specific stream with data in that packet is blocked
## Adjustments required
- new compression scheme called QPACK to cater for the unique characteristics