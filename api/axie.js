export default async function handler(req, res) {
  const { id } = req.query;

  const query = `
    query {
      axie(axieId: "${id || "11358166"}") {
        axpStatDay {
          axieId
          axpAxieCapDay
          totalGainedAxpDay
        }
      }
    }
  `;

  try {
    const response = await fetch("https://graphql-gateway.axieinfinity.com/graphql", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    const data = await response.json();
    res.status(200).json(data);

  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}
