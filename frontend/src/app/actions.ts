export async function getLinks() {
  const url = process.env.API_URL as string;
  const res = await fetch(url);
  const links = await res.json();
  return links;
}
