const renderToBoard = (content, imgUrl) => {
    const root = document.querySelector("#root");
    const p = document.createElement("p");
    const img = document.createElement("img");
    const hr = document.createElement("hr");
    p.textContent = content;
    img.src = imgUrl;
    root.appendChild(hr);
    root.appendChild(img);
    root.appendChild(p);
};

const upload = () => {
    const submit = document.querySelector("input[type='submit']");
    submit.addEventListener("click", async () => {
        const content = document.querySelector("#content").value;
        const imageFile = document.querySelector("#image").files[0];
        const formData = new FormData();
        formData.append("content", content);
        formData.append("file", imageFile);
        // s3 & rds
        const resp = await fetch("/api/upload", {
            method: "PATCH",
            body: formData,
        });
        const resp_json = await resp.json();
        if (resp_json["ok"]) {
            const data = await downloadOne();
            renderToBoard(data[0], data[1]);
        }
    });
};

const downloadAll = async () => {
    const resp = await fetch("/api/download_all");
    const data = await resp.json();
    return data["data"];
};

const downloadOne = async () => {
    const resp = await fetch("/api/download_one");
    const data = await resp.json();
    return data["data"];
};

const initloding = async () => {
    const datas = await downloadAll();
    datas.forEach((data) => {
        renderToBoard(data[0], data[1]);
    });
};

// mainExe
initloding();
upload();
