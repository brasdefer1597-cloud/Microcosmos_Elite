module.exports = (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.status(200).json({ 
    status: "SYNC_OK", 
    node: "XALAPA_BUNKER",
    timestamp: new Date().toISOString()
  });
};
