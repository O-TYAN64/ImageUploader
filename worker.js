export default {
  async fetch(request, env, ctx) {
    if (request.method === "POST") {
      const formData = await request.formData();
      const file = formData.get("file");
      if (!file || typeof file === "string") {
        return new Response("No file uploaded", { status: 400 });
      }
      const filename = `${Date.now()}-${file.name}`;
      await env.MY_BUCKET.put(filename, file.stream(), {
        httpMetadata: {
          contentType: file.type,
        },
      });
      return new Response(`File uploaded as ${filename}`, { status: 200 });
    }

    return new Response("Method not allowed", { status: 405 });
  }
};

