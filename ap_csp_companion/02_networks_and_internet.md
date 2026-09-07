# Networks and the Internet

**Suggested time:** 1-2 class periods  
**Connects to:** file transfer, client-server programs, APIs, and asyncio

## Learning Goals

- Model how messages travel between devices through interconnected networks.
- Explain why Internet protocols allow independently designed systems to
  communicate.
- Describe how redundancy and routing can make a network more fault tolerant.
- Identify a tradeoff among speed, reliability, privacy, and cost.

## Activity

1. In groups, model a network of six devices with paper nodes and message
   cards. Create at least two routes between the sender and receiver.
2. Send a message through the network. Remove one connection midway and route
   a new message without using that connection.
3. Create a simple message format that every group must use:

   ```text
   FROM: <sender>
   TO: <recipient>
   BODY: <message>
   ```

   Discuss what happens when a group changes the format without agreement.
4. Write a short explanation of how packets, protocols, and redundant routes
   relate to your model. Do not claim that every real network always finds a
   route; explain that redundancy improves the chance of delivery.

## Student Deliverable

Submit a labeled network diagram and a 150-250 word explanation answering:

- How did the message reach its destination?
- What changed after a connection failed?
- Why did the shared format matter?
- What tradeoff did your design make?

## Evidence Checklist

- The diagram shows at least two possible routes before the simulated failure.
- The explanation connects the model to protocols and fault tolerance.
- The tradeoff is specific rather than simply saying one design is “better.”

