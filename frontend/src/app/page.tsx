import { getLinks } from "./actions";

const Page = async ()=> {
  const links = await getLinks()

  console.log(links);
  return (
    <div className="bg-red-500">
      Hello world anik
    </div>
  )
}

export default Page;
